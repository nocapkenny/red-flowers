<script setup>
import { useRoute } from 'vue-router'
const $route = useRoute()


</script>

<template>
  <nav class="navbar navbar-expand-lg ">
    <div class="container-fluid">
      <a href="#" class="navbar-brand"> Красная Гвоздика </a>
      <!-- бургер меню -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.path === '/' }" to="/">Главная</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.path === '/about' }" to="/about">О нас</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.path === '/catalog' }" to="/catalog">Каталог</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.path === '/prices' }" to="/prices">Прайс-лист</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.path === '/gallery' }" to="/gallery">Галерея</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.path === '/vacancies' }" to="/vacancies">Вакансии</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.path === '/articles' }" to="/articles">Статьи</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.path === '/contacts' }" to="/contacts">Контакты</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar{
  box-shadow: 0px 5px 10px 2px rgba(34, 60, 80, 0.2);
  padding-top: 15px;
  padding-bottom: 15px;
}
.navbar-brand{
  margin-right: 80px;
}
.nav-link{
  font-size: 18px !important;
  color: var(--default);
}

.nav-link:hover{
  color: var(--red) !important;
}
.active {
  color: var(--red) !important;
}
</style>
