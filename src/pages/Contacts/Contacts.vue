<script setup>
import Header from "../../components/Header/Header.vue";
</script>

<template>
  <Header />
  <div class="contacts container">
    <h3 class="contacts__title title">Контакты</h3>
    <div class="contacts__inner">
      <div class="contacts__box">
        <p class="contacts__box-title">Информация</p>
        <p class="contacts__box-descr contacts__box-descr--address">Адрес</p>
        <ul class="contacts__list">
          <li class="contacts__list-item">
            д. Башкултаево, Пермский край (30 км от г. Перми)
          </li>
        </ul>
        <p class="contacts__box-descr contacts__box-descr--connect">
          Связать с нами
        </p>
        <ul class="contacts__list">
          <li class="contacts__list-item">
            <span>Менеджер Анастасия: </span
            ><a href="tel:89226406683" class="contacts__list-link"
              >+7(922)-640-66-83</a
            >
          </li>
          <li class="contacts__list-item">
            <span>Менеджер Ирина: </span
            ><a href="tel:89226408604" class="contacts__list-link"
              >+7(922)-640-86-04</a
            >
          </li>
          <li class="contacts__list-item">
            <span>Директор Черепанова В. И.: </span
            ><a href="tel:89824718876" class="contacts__list-link"
              >+7(982)-471-88-76</a
            >
          </li>
          <li class="contacts__list-item">
            <span>Директор Черепанова В. И.: </span
            ><a
              href="mailto:krasnaya-gvozdika@yandex.ru"
              class="contacts__list-link"
              >krasnaya-gvozdika@yandex.ru</a
            >
          </li>
        </ul>
        <p class="contacts__box-descr contacts__box-descr--work">
          Режим работы
        </p>
        <ul class="contacts__list">
          <li class="contacts__list-item">
            <span>Понедельник-Воскресенье: </span> 09:00 - 19:00
          </li>
        </ul>
      </div>
      <div class="contacts__box">
        <form class="contacts__form">
          <p class="contacts__form-title">Написать нам</p>
          <input
            type="text"
            class="contacts__form-input"
            placeholder="Тема сообщения"
          />
          <input
            type="email"
            class="contacts__form-input"
            placeholder="Ваш Email"
          />
          <textarea
            class="contacts__form-textarea"
            placeholder="Cообщение"
          ></textarea>
          <button class="contacts__form-btn btn">Отправить</button>
        </form>
      </div>
    </div>
    <!-- тут можно iframe с картой -->
    <img
      src="../../assets/images/map.jpg"
      alt="map"
      class="contacts__box-img"
    />
  </div>
</template>

<style src="./Contacts.scss" scoped />
