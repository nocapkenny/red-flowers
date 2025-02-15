<script setup>
<<<<<<< HEAD
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
const $route = useRoute();

const isMenuOpen = ref(false);
=======
import { useRoute } from "vue-router";
const $route = useRoute();
>>>>>>> 8e0ab739f64b0bbd314ac9aa75f85d58fe4b629b
</script>

<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a href="#" class="navbar-brand">
<<<<<<< HEAD
        <img src="../../assets/images/logo.jpg" alt="logo" width="60" />
      </a>
      <!-- бургер меню -->
      <button
        @click="isMenuOpen = !isMenuOpen"
=======
        <img src="../../assets/images/logo.jpg" alt="logo" width="60"/>
      </a>
      <!-- бургер меню -->
      <button
>>>>>>> 8e0ab739f64b0bbd314ac9aa75f85d58fe4b629b
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
<<<<<<< HEAD
      <div
        class="mobile-menu collapse"
        :class="{ show: isMenuOpen }"
        id="mobileMenu"
      >
        <ul class="navbar-nav flex-column">
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/' }"
              to="/"
              @click="isMenuOpen = false"
              >Главная</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/about' }"
              to="/about"
              @click="isMenuOpen = false"
              >О нас</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/catalog' }"
              to="/catalog"
              @click="isMenuOpen = false"
              >Каталог</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/prices' }"
              to="/prices"
              @click="isMenuOpen = false"
              >Прайс-лист</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/gallery' }"
              to="/gallery"
              @click="isMenuOpen = false"
              >Галерея</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/vacancies' }"
              to="/vacancies"
              @click="isMenuOpen = false"
              >Вакансии</router-link
            >
          </li>
          <!-- <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/articles' }"
              to="/articles"
              @click="isMenuOpen = false"
              >Статьи</router-link
            >
          </li> -->
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/contacts' }"
              to="/contacts"
              @click="isMenuOpen = false"
              >Контакты</router-link
            >
          </li>
        </ul>
      </div>
=======
>>>>>>> 8e0ab739f64b0bbd314ac9aa75f85d58fe4b629b
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/' }"
              to="/"
              >Главная</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/about' }"
              to="/about"
              >О нас</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/catalog' }"
              to="/catalog"
              >Каталог</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/prices' }"
              to="/prices"
              >Прайс-лист</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/gallery' }"
              to="/gallery"
              >Галерея</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/vacancies' }"
              to="/vacancies"
              >Вакансии</router-link
            >
          </li>
          <!-- <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/articles' }"
              to="/articles"
              >Статьи</router-link
            >
          </li> -->
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: $route.path === '/contacts' }"
              to="/contacts"
              >Контакты</router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style src="./Header.scss" scoped />
