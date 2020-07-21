// let boxes = {};

// window.onload = () => {
//   Promise.all([
//     fetch("http://127.0.0.1:8000/videos/1")
//       .then((response) => response.json())
//       .then((data) => (boxes = data["metadata"]["boxes"])),
//     fetch("http://127.0.0.1:8000/videos/2")
//       .then((response) => response.json())
//       .then((data) => (boxes[1] = data["metadata"]["boxes"])),
//   ]);
// };

class VideoPlayer {
  constructor(id) {
    this.video = document.querySelector(`#video-${id}`);
    this.button = document.querySelector(`#button-${id}`);
    this.progress = document.querySelector(`#progress-${id}`);

    this.canvas = document.querySelector(`#canvas-${id}`);
    this.ctx = this.canvas.getContext("2d");

    this.metadata = { fps: 7.5 };
    fetch(`http://127.0.0.1:8000/videos/${id}`)
      .then((response) => response.json())
      .then((data) => {
        this.metadata.boxes = data["metadata"]["boxes"];
      });

    this.video.onplay = () => {
      this.frameCallback();
    };

    this.video.ontimeupdate = () => {
      if (!this.progress.getAttribute("max"))
        this.progress.setAttribute("max", this.video.duration);
      this.progress.value = this.video.currentTime;
    };

    this.button.onclick = (e) => {
      if (this.video.paused) {
        this.video.play();
        e.target.innerHTML = "Pause";
      } else {
        this.video.pause();
        e.target.innerHTML = "Play";
      }
    };

    this.progress.onclick = (e) => {
      let offset =
        this.progress.offsetLeft + this.progress.offsetParent.offsetLeft;
      let pos = (e.pageX - offset) / this.progress.offsetWidth;
      this.video.currentTime = pos * this.video.duration;
      if (this.video.paused || this.video.ended) {
        this.computeFrame();
      }
    };
  }

  frameCallback = () => {
    if (this.video.paused || this.video.ended) {
      return;
    }

    this.computeFrame();
    requestAnimationFrame(this.frameCallback);
  };

  computeFrame = () => {
    let rect = this.video.getBoundingClientRect();
    this.canvas.width = rect.width;
    this.canvas.height = rect.height;
    this.ctx.strokeStyle = "lime";
    this.ctx.fillStyle = "lime";
    this.ctx.lineWidth = "2";
    this.ctx.font = "15px Arial";
    //this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    let frame_idx = Math.ceil(this.video.currentTime * this.metadata.fps);
    if (frame_idx in this.metadata.boxes) {
      this.metadata.boxes[frame_idx].forEach((box) => {
        let left = (box[0] / 1000) * rect.width;
        let top = (box[1] / 1000) * rect.height;
        let width = (box[2] / 1000) * rect.width;
        let height = (box[3] / 1000) * rect.height;
        this.ctx.strokeRect(left, top, width, height);
        this.ctx.fillText(box[4], left + width / 2, top + height / 2);
      });
    }
  };
}

player1 = new VideoPlayer(1);
player2 = new VideoPlayer(2);
