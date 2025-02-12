<script setup>
import Header from "../../components/Header/Header.vue";
import GalleryGroup from "../../components/GalleryGroup/GalleryGroup.vue";

const galleries = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 1];
</script>

<template>
  <Header />
  <div class="gallery">
    <div class="container">
      <h3 class="gallery__title title">Галерея</h3>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="gallery in galleries">
          <GalleryGroup />
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_mixins" as *;
@use "../../assets/sytles/_vars" as *;
.gallery {
  @include bg-section("../../assets/images/gallery-bg.jpg");
  padding-top: 50px;
  padding-bottom: 50px;
  &__title {
    color: $white;
  }
}
</style>
