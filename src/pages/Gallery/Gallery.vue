<script setup>
import Header from "../../components/Header/Header.vue";
import GalleryGroup from "../../components/GalleryGroup/GalleryGroup.vue";
import { useGalleryStore } from "@/stores/galleryStore";
import { onMounted } from "vue";
const galleryStore = useGalleryStore();
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


onMounted(() => {
  galleryStore.getGalleryCategory();
})
</script>

<template>
  <Header />
  <section class="gallery">
    <div class="container">
      <h3 class="gallery__title title">Галерея</h3>
      <div class="row row-cols-1 row-cols-md-3 g-4" v-if="galleryStore.galleryCategory" v-auto-animate>
        <div class="col" v-for="gallery in galleryStore.galleryCategory" >
          <GalleryGroup :id="gallery.id" :name="gallery.name" :bg="gallery.first_image"/>
        </div>
      </div>
    </div>
  </section>
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
