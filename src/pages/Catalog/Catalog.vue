<script setup>
import { ref } from "vue";
import Header from "../../components/Header/Header.vue";
import CardList from "../../components/CardList/CardList.vue";
import Filters from "../../components/Filters/Filters.vue";
import Search from "@/components/Search/Search.vue";
</script>

<template>
  <Header />
  <Search />
  <div class="catalog">
    <Filters />
    <CardList />
  </div>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_mixins" as *;
.catalog {
  @include bg-section("../../assets/images/catalog-bg.jpg");
  padding-left: 20px;
  padding-right: 20px;
  flex-direction: row;
  align-items: normal;
}
</style>
