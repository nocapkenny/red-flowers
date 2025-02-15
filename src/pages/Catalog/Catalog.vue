<script setup>
import { ref } from "vue";
import Header from "../../components/Header/Header.vue";
import CardList from "../../components/CardList/CardList.vue";
import Filters from "../../components/Filters/Filters.vue";

const isBigCard = ref(false);
</script>

<template>
  <Header />
  <div class="catalog">
    <Filters v-model:isBigCard="isBigCard" />
    <CardList :isBigCard="isBigCard" />
  </div>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_mixins" as *;
.catalog {
  @include bg-section("../../assets/images/catalog-bg.jpg");
}
</style>
