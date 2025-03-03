<script setup>
import Header from "@/components/Header/Header.vue";
import GalleryList from "@/components/GalleryList/GalleryList.vue";
</script>

<template>
  <Header />
  <section class="gallery-detail">
    <div class="container">
      <GalleryList />
    </div>
  </section>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_vars" as *;
@use "../../assets/sytles/_mixins" as *;
.gallery-detail {
  padding-top: 50px;
  @include bg-section("../../assets/images/gallery-bg.jpg");
}
</style>
