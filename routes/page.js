const express = require('express');
const { isLoggedIn } = require('./middlewares');

const router = express.Router();

router.use((req, res, next) => {
    res.locals.user = req.user;
    next();
})

router.get('/', (req, res, next) =>{
    res.render('totalJipyo.html');
})

router.get('/stockJipyo', isLoggedIn, (req, res, next) => {
    res.render('stockJipyo.html');
})

router.get('/join', (req, res) => {
    res.render('register');
})

router.get('/login', (req, res) =>{
    res.render('login');
})


module.exports = router;