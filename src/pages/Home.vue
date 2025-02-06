<script setup>
import Header from "../components/Header.vue";
</script>

<template>
  <Header />
  <div class="home">
    <div class="home__box">
      <h1 class="home__title">
        Добро пожаловать в питомник <br />
        Красная Гвоздика
      </h1>
      <router-link class="home__link" to="/catalog">Каталог</router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use "../assets/sytles/_vars" as *;
.home {
  display: flex;
  flex-direction: column;
  min-height: calc(100vh - 73px);
}
.home__box {
  flex-grow: 1;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/images/home-bg.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  color: $white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.home__title {
  text-align: center;
  color: $white;
  font-size: 54px;
}
.home__link {
  display: inline-block;
  background-color: $red;
  color: $white;
  padding: 10px 25px;
  font-size: 24px;
  text-decoration: none;
  border-radius: 5px;
  margin-top: 30px;
  transition: all 0.3s ease;
}

.home__link:hover {
  background-color: $white;
  color: $red;
}
</style>
