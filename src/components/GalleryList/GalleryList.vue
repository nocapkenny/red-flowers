<script setup>
import { useGalleryStore } from "@/stores/galleryStore";
import { useRoute } from "vue-router";
import { onMounted } from "vue";
const galleryStore = useGalleryStore();
const $route = useRoute();

onMounted(() => {
  galleryStore.getGalleryImagesByCategory($route.params.id);
});
</script>

<template>
  <div class="gallery-list" v-if="galleryStore.galleryImages">
    <div class="container">
      <div class="row g-4">
        <div
          class="col-12 col-sm-6 col-md-4 col-lg-3"
          v-for="image in galleryStore.galleryImages"
        >
          <div class="gallery-list__item">
            <img
              class="gallery-list__image"
              :src="image.image"
              alt="galleryImage"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_vars" as *;
.gallery-list {
  &__item{
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: $shadow;
    transition: all 0.3s ease;
  }
  &__item:hover{
    transform: scale(1.05);
  }
  &__image{
    width: 100%;
    height: 500px;
    object-fit: cover;
    border-radius: 8px;
  }
}
</style>
