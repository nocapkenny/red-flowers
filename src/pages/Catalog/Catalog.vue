<script setup>
import { ref } from "vue";
import Header from "../../components/Header/Header.vue";
import CardList from "../../components/CardList/CardList.vue";
import Filters from "../../components/Filters/Filters.vue";

</script>

<template>
  <Header />
  <div class="catalog">
      <Filters />
      <CardList />
  </div>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_mixins" as *;
.catalog {
  // @include bg-section("../../assets/images/catalog-bg.jpg");
  display: flex;
}
</style>
