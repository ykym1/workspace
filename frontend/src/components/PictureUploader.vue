<template>
  <v-container>
    <v-row dense>
      <input type="file" ref="file" @change="setImage" />
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "PictureUploader",

  data: () => ({
    file: null,
    fileData: null,
  }),
  methods: {
    setImage() {
      const files = this.$refs.file;
      const file = files.files[0];

      const self = this;
      const reader = new FileReader();
      reader.addEventListener(
        "load",
        function () {
          // 画像ファイルを base64 文字列に変換
          self.$emit("capturedImage", reader.result);
        },
        false
      );

      reader.readAsDataURL(file);
    },
  },
};
</script>
