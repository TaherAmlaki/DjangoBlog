const homeCanvas = document.getElementById('home-canvas');
const ctx = homeCanvas.getContext('2d');
const lineColor = '#6da2f2'
var maxLevel = 5;
var branches = 2;
const angle = Math.PI * 2 * 0.97;
var deltaAngle = 0.25
const scaleFactor = 0.7;
const sides = 2;
const lineWidth = 1.5;
homeCanvas.width = window.innerWidth;
homeCanvas.height = window.innerHeight;
var translateLen = Math.floor(homeCanvas.width / 3);
var lineLen = translateLen * 1.0;
ctx.translate(homeCanvas.width/2, homeCanvas.height/2);

var positiveAngle = angle + deltaAngle;
var negativeAngle = angle - deltaAngle;

function drawLine(level){
  if (maxLevel < level) return;

  ctx.strokeStyle = lineColor;
  ctx.lineWidth = lineWidth;
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.lineTo(lineLen, 0);
  ctx.stroke();

  for(var i=1; i<branches + 1; i++){
    ctx.save();
    ctx.translate(translateLen * i / (branches + 1), 0);
    ctx.scale(scaleFactor, scaleFactor);
    ctx.save();

    ctx.rotate(positiveAngle);
    drawLine(level+1);
    ctx.restore();
    ctx.save()

    ctx.rotate(-negativeAngle);
    drawLine(level+1);
    ctx.restore();

    ctx.restore();
  }
}

function init(){
  ctx.clearRect(0, 0, innerHeight, innerHeight);
  for (let i =0; i < sides; i++){
    drawLine(0);
    ctx.rotate(Math.PI * 2 / sides);
  }
}


function getWidthAndHeight(){
  homeCanvas.width = window.innerWidth;
  homeCanvas.height = window.innerHeight;
  translateLen = Math.floor(homeCanvas.width / 3);
  lineLen = translateLen * 1.0;
  ctx.translate(homeCanvas.width/2, homeCanvas.height/2);
  if (homeCanvas.width < 500){
    maxLevel = 3;
    lineLen = translateLen * 1.0;
  } else {
    maxLevel = 5;
    lineLen = translateLen * 1.0;
  }
  console.log("resize event", maxLevel);
  console.log(homeCanvas.width, homeCanvas.height);
  init();
}

window.addEventListener('resize', getWidthAndHeight);

init();
