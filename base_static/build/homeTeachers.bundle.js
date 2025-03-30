/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./base_static/global/js/teachersHome.js":
/*!***********************************************!*\
  !*** ./base_static/global/js/teachersHome.js ***!
  \***********************************************/
/***/ (() => {

eval("(function () {\n  var larguraTela = window.innerWidth;\n  if (larguraTela <= 500) {\n    var elementDisplay = document.querySelector('.alert-mobile').style.display = 'block';\n  }\n  var span = document.querySelector('.cumprimento');\n  var atualDate = new Date().getHours();\n  if (atualDate >= 6 && atualDate < 12) span.innerHTML = 'Bom dia';else if (atualDate >= 12 && atualDate < 18) span.innerHTML = 'Boa tarde';else if (atualDate >= 18 && atualDate < 24 || atualDate < 6) span.innerHTML = 'Boa noite';else span.innerHTML = 'Olá';\n})();\n\n//# sourceURL=webpack://ed_planejamentos/./base_static/global/js/teachersHome.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./base_static/global/js/teachersHome.js"]();
/******/ 	
/******/ })()
;