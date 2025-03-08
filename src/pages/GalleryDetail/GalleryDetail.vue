<script setup>
import Header from "@/components/Header/Header.vue";
import GalleryList from "@/components/GalleryList/GalleryList.vue";
import { useHead } from "@vueuse/head";

useHead({
  title: 'Питомник "Красная Гвоздика"',
  meta: [
    { name: "description", content: 'питомник растений "Красная Гвоздика"' },
    {
      name: "keywords",
      content:
        "цветы, растения, саженцы, кустарники, деревья, купить саженцы, купить растения",
    },
  ],
});
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
