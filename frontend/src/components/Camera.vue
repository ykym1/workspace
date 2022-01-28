<template>
  <v-container>
    <div>
      <video
        ref="video"
        id="video"
        :width="width"
        autoplay
        style="-webkit-transform: scaleX(-1)"
      ></video>
      <div>
        <v-btn color="info" id="snap" v-on:click="capture()">
          Snap Photo
        </v-btn>
      </div>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "Camera",
  data: () => ({
    video: {},
    canvas: {},
    // width: window.innerWidth,
    width: 351,
  }),
  mounted() {
    this.video = this.$refs.video;
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
        this.video.srcObject = stream;
        this.video.play();
      });
    }

    // window.addEventListener("resize", this.resize);
  },
  beforeDestroy() {
    // window.removeEventListener("resize", this.resize);
  },
  methods: {
    resize() {
      this.width = window.innerWidth;
    },
    capture() {
      let newCanvas = document.createElement("canvas");
      newCanvas.width = 260;
      newCanvas.height = 195;
      newCanvas.ref = "canvas";
      newCanvas.id = "canvas";

      this.canvas = newCanvas;
      const ctx = this.canvas.getContext("2d");
      ctx.scale(-1, 1);
      ctx.translate(-this.canvas.width, 0);
      ctx.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height);

      this.$emit("capturedImage", this.canvas.toDataURL("image/jpeg"));
    },
  },
};
</script>
