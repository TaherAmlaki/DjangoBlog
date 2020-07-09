const canvas = document.getElementById('education-canvas');
const context = canvas.getContext('2d');
const particlesColor = '#8ee366'
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let s3 = 1.73205080757
let a = 75;
let connectMax = 1.2 * a * a
let movement = 0.07
let a1x = 1.5 * a;
let a1y = s3 * a * 0.5;
let dx = -a;
let nx = canvas.width / a1x
let xc = canvas.width * 0.5;
let yc = canvas.height * 0.5;
let pi2 = Math.PI * 2;

// creating the random particles
let particlesArray;
class Particle{
  constructor(x, y, size, color){
    this.x = x;
    this.y = y;
    this.size = size;
    this.color = color;
  }

  draw(){
    context.beginPath();
    context.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
    context.fillStyle = particlesColor;
    context.fill();
  }

  update(){
    if(this.x > canvas.width || this.x < 0){
      this.dirX = -this.dirX;
    }
    if(this.y > canvas.height || this.y < 0){
      this.dirY = -this.dirY;
    }
    let vr = Math.random()
    this.x += movement * Math.sin(pi2 * vr);
    this.y += movement * Math.cos(pi2 * vr);
    this.draw();
  }
}

function init(){
  particlesArray = [];
  let numberOfParticles = (canvas.height * canvas.width) / 9000;

  for(let i=0; i < nx; i++){
    for(let j=0; j < nx; j++){
      let x = (i + j - nx) * a1x + xc
      let y = (i - j) * a1y + yc
      particlesArray.push(new Particle(x, y, 5, particlesColor));
      particlesArray.push(new Particle(x + dx, y, 5, particlesColor));
    }
  }
}

function animate(){
  requestAnimationFrame(animate);
  context.clearRect(0, 0, innerWidth, innerHeight);
  for (let i=0; i<particlesArray.length; i++){
    particlesArray[i].update();
  }
  connect();
}

function connect(){
  let opacityValue = 1;
  for (let p1=0; p1 < particlesArray.length; p1++){
    for(let p2=p1+1; p2< particlesArray.length; p2++){
      let dx = particlesArray[p1].x - particlesArray[p2].x;
      let dy = particlesArray[p1].y - particlesArray[p2].y;
      let dis = dx * dx + dy * dy;
      if (dis < connectMax){
        opacityValue = 1 - (dis/20000);
        context.strokeStyle = 'rgba(140, 85, 31, ' + opacityValue + ')';
        context.lineWidth = 1;
        context.beginPath();
        context.moveTo(particlesArray[p1].x, particlesArray[p1].y);
        context.lineTo(particlesArray[p2].x, particlesArray[p2].y);
        context.stroke();
      }
    }
  }
}

function getWidthAndHeight(){
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  xc = canvas.width * 0.5;
  yc = canvas.height * 0.5;
}

window.addEventListener('resize', getWidthAndHeight);

init();
animate();
