<script setup>
import Header from "../../components/Header/Header.vue";
import GalleryGroup from "../../components/GalleryGroup/GalleryGroup.vue";

const galleries = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 1];
</script>

<template>
  <Header />
  <div class="gallery container">
    <h3 class="gallery__title">
        Галерея
    </h3>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div class="col" v-for="gallery in galleries">
        <GalleryGroup />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.gallery {
    &__title {
        text-align: center;
        font-size: 32px;
        margin-bottom: 30px;
    }
  padding-top: 50px;
  padding-bottom: 50px;
}
</style>
