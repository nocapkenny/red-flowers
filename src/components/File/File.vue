<script setup>
import { onMounted } from "vue";
import DownloadSvg from "../../assets/images/download.svg";
const props = defineProps({
  filePath: {
    type: String,
    required: true,
  },
  fileName: {
    type: String,
    required: true,
  }
});

const downloadFile = () => {
  const link = document.createElement("a");
  link.href = props.filePath;
  link.setAttribute = document.createAttribute("download", props.fileName);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

onMounted(() => {
  console.log(props.link);
})
</script>

<template>
  <div class="file">
    <DownloadSvg class="file__svg" />
    <p class="file__name">{{ fileName }}</p>
    <button @click="downloadFile" class="file__btn btn">Скачать</button>
  </div>
</template>

<style src="./File.scss" scoped />
