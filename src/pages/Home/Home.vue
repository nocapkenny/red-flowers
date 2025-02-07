<script setup>
import Header from "../../components/Header/Header.vue";
</script>

<template>
  <Header />
  <div class="home">
    <h1 class="home__title">
      Добро пожаловать в питомник <br />
      Красная Гвоздика
    </h1>
    <router-link class="home__link" to="/catalog">Каталог</router-link>
  </div>
</template>

<style src="./Home.scss" scoped />
