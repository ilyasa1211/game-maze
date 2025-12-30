const canvas = document.getElementById('scratchpad');

if (!canvas) {
  throw new Error("canvas with id scratchpad not found");
}

/**
 * @type CanvasRenderingContext2D | null
 */
const ctx = canvas.getContext('2d');

if (!ctx) {
  throw new Error("failed to create")
}

const passage = "p";
const wall = "w";
const width = canvas.dataset.width;
const heigth = canvas.dataset.height;
const cellWidth = canvas.dataset.cellWidth;
const cellHeigth = canvas.dataset.cellHeight;
const raw = canvas.dataset.data;

if (typeof width === "undefined" || typeof heigth === "undefined" || typeof raw === "undefined"
  || typeof cellWidth === "undefined" || typeof cellHeigth === "undefined"
) {
  throw new Error("width or height is undefined")
}


const actualWidth = width * 2 + 1;
const actualHeight = heigth * 2 + 1;
const maze = raw.split("")

canvas.width = actualWidth * cellWidth;
canvas.height = actualHeight * cellHeigth;
/**
 * @type null | number
 */
let requestAnimationFrameId = null;

function update() {
  ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight)

  for (const [i, v] of maze.entries()) {
    const x = i % actualWidth * cellWidth;
    const y = Math.floor(i / actualWidth) * cellHeigth;

    if (v === wall) {
      ctx.beginPath()
      ctx.fillStyle = "#202020"
      ctx.fillRect(x, y, cellWidth, cellHeigth)
    }

    if (v === passage) {
      ctx.fillStyle = "#aaaaaa"
      ctx.fillRect(x, y, cellWidth, cellHeigth)
    }
  }
}

function start() {
  update()
  requestAnimationFrameId = requestAnimationFrame(start)
}

start()





