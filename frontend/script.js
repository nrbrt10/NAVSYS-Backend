window.onload = init()

function init(){
  const canvas = document.getElementById("map");
  const ctx = canvas.getContext("2d")
  const gridsInViewList = document.getElementById("gridsInViewList")
  let isDragging = false;
  const worldViewport = {x: 0, y: 0} // current viewport origin in world

  window.requestAnimationFrame(gameLoop);
}

async function gameLoop(){
  update();
  draw();

  window.requestAnimationFrame(gameLoop);
}

function update(){
  const grids = {};
  fetchData();
  populateGridsInView();
}

function draw(){
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.save();

  ctx.translate(-worldViewport.x, -worldViewport.y)

  for(const uuid in grids) {
    const color = grids[uuid].color;
    const positions = grids[uuid].positions;

    positions.forEach((pos, index) => {
      const {x: canvasX, y: canvasY} = toCanvasCoords(pos);

      ctx.beginPath();
      ctx.arc(canvasX, canvasY, 5, 0 , 2 * Math.PI);
      ctx.fillStyle = `rgba(${color.r}, ${color.g}, ${color.b}, ${0.3 + index * 0.3})`;
      ctx.fill();
    });
  }
  ctx.restore();
}

async function fetchData(){
  const response = await fetch("http://localhost:8000/api/v1/grid_positions/latest/");
  const data = await response.json();

  data.forEach(({uuid, grid_name, x, y}) => {
    if (!grids[uuid]) {
      grids[uuid] = {
        name: grid_name,
        color: {r: getRandomColor(), g: getRandomColor(), b: getRandomColor()},
        positions: [],
      };
    }
    grids[uuid].push({x, y});
  });
}

function populateGridsInView(){
  gridsInViewList.innerHTML = '';

  Object.keys(grids).forEach((uuid) => {
    const grid = document.createElement("li");
    const { gridName, color, positions } = grids.uuid;
    const lastPos = positions[positions.length - 1];
    grid.id = uuid;
    grid.style.color = `rgb(${color.r}, ${color.g}, ${color.b})`;
    grid.textContent = `${gridName} - ${uuid}: ${lastPos.x}:${lastPos.y}`;
    grid.addEventListener('click', () => {
      centerOnGrid(lastPos.x, lastPos.y);
    });
    gridsInViewList.appendChild(grid);
  }
)};

function centerOnGrid(x, y){
  worldViewport.x = x - canvas.width/2;
  worldViewport.y = y - canvas.height/2;
}

canvas.addEventListener('mousedown', (event) => {
  isDragging = true;
  startX = event.clientX;
  startY = event.clientY;
});

canvas.addEventListener('mousemove', (event) => {
  if (isDragging){
    panningHandler(event);
  } else {
    getCurrentPosition(event);
  }
});

canvas.addEventListener('mouseup', () => {
  isDragging = false;
})

function toCanvasCoords(pos){
  return {x: pos.x, y: -pos.y}
}


function getRandomColor(){
  return Math.floor(Math.random() * 255);
}