<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";
const $router = useRouter();

const props = defineProps({
  name: {
    type: String,
    required: true
  },
  id: {
    type: Number,
    required: true
  },
  bg: {
    type: String,
    required: true
  }
})

const goToGallery = () => {
  $router.push({
    name: 'gallery-detail',
    params: {
      id: props.id
    }
  })
}

</script>

<template>
  <div class="gallery-group" @click="goToGallery">
    <img :src="'http://127.0.0.1:8000' + bg" />
    <div class="gallery-group__overlay">
        <h4 class="gallery-group__title">
            {{ name }}
        </h4>
    </div>
  </div>
</template>

<style src="./GalleryGroup.scss" scoped></style>
