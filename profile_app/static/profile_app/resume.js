const resumeCanvas = document.getElementById('resume-canvas');
const ctx = resumeCanvas.getContext('2d');
resumeCanvas.width = window.innerWidth;
resumeCanvas.height = window.innerHeight;
var canvasArea = resumeCanvas.width * resumeCanvas.height;

var maxSize = 10;
var minSize = 5;
const colors = [
  'white',
  'rgba(242, 48, 22, 0.2)',
  'rgba(70, 167, 10, 0.4)',
  'rgba(173, 216, 230, 0.8)',
  'rgba(211, 211, 211, 0.8)'
]


let particles = [];
class Particle{
  constructor(x, y, size, color){
    this.x = x;
    this.y = y;
    this.size = size;
    this.color = color;
  }
  draw(){
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
    ctx.fillStyle = this.color;
    ctx.fill();
  }
}

function connect(){
  for(let p1=0; p1<particles.length; p1++){
    for(let p2=p1; p2<particles.length; p2++){
      let dx = particles[p1].x - particles[p2].x;
      let dy = particles[p1].y - particles[p2].y;
      let dis = Math.pow(dx, 2) + Math.pow(dy, 2);
      if (dis < canvasArea / 75){
        ctx.strokeStyle = '#e6d709';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(particles[p1].x, particles[p1].y);
        ctx.lineTo(particles[p2].x, particles[p2].y);
        ctx.stroke();
      }
    }
  }
}

function init(){
  ctx.clearRect(0, 0, innerHeight, innerHeight);

  particles = [];
  let numberOfParticles = 200;
  for (let i=0; i<numberOfParticles; i++){
    let size = Math.floor(Math.random() * (maxSize - minSize) + minSize);
    let x = (Math.random() * (innerWidth - 2 * size * 2) + size * 2);
    let y = (Math.random() * (innerHeight - 2 * size * 2) + size * 2);
    let color = "#e6d709";  //colors[Math.floor(Math.random() * (colors.length-1)+1)];
    particles.push(new Particle(x, y, size, color));
    particles[i].draw();
  }
  connect();
}

window.addEventListener('resize', function(){
  resumeCanvas.width = window.innerWidth;
  resumeCanvas.height = window.innerHeight;
  canvasArea = resumeCanvas.width * resumeCanvas.height;
  init();
})

init();
