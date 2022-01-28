<template>
  <v-app>
    <PictureUploader @capturedImage="editImage" />
    <Camera v-if="isSmartPhone" @capturedImage="editImage" />
    <v-container><img :src="img" width="351" /></v-container>
  </v-app>
</template>

<script>
import PictureUploader from "./components/PictureUploader";
import Camera from "./components/Camera";

export default {
  name: "App",
  components: {
    PictureUploader,
    Camera,
  },
  data: () => ({
    testName: "",
    img: "",
    isSmartPhone: false,
  }),
  mounted() {
    if (navigator.userAgent.match(/iPhone|Android.+Mobile/)) {
      this.isSmartPhone = false;
    } else {
      this.isSmartPhone = true;
    }
  },
  methods: {
    async editImage(capturedImage) {
      await this.axios
        .post("/editImage", {
          image: capturedImage,
        })
        .then((response) => {
          this.img = response.data.image;
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
