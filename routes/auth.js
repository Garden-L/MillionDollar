const express = require('express');
const passport = require('passport');
const User = require('../models/user');
const getPbkdf2 = require('../util/getPbkdf2');
const crypto = require('crypto');
const { isLoggedIn, isNotLoggedIn } = require('./middlewares');

const router = express.Router();

router.post('/join', isNotLoggedIn, async (req, res, next) => {
    const {id, email, password1, password2} = req.body;

    if (password1 !== password2) {
        return res.redirect('/join');
    }

    try{
        const exUser = await User.findOne({where: {id}});

        if (exUser){
            return res.redirect('/join?error=exist');
        }

        const salt = crypto.randomBytes(64).toString('Base64');
        const hash = await getPbkdf2(password1, salt, 10908, 64, 'sha256');
        const base = hash.toString('Base64');

        await User.create({
            id: id,
            email: email,
            password: base,
            salt: salt,
        });

        return res.redirect('/');
    } catch (err){
        console.log(err);
        return next(err);
    }
});

router.post('/login', isNotLoggedIn, (req, res, next) => {
    passport.authenticate('local', (authError, user, info) => {
        if(authError) {
            console.error(authError);
            return next(authError);
        }

        if(!user){
            return res.redirect('/join');
        }

        return req.login(user, (loginError)=> {
            if(loginError){
                console.error(loginError);
                return next(loginError);
            }

            return res.redirect('/');
        });
    })(req, res, next);
});

router.get('/logout', isLoggedIn, (req, res) => {
    req.logout((err) => {
        if(err){
            return res.send('오류');
        }
        req.session.destroy((err) =>{
            res.clearCookie('connect.sid');
            res.clearCookie('cook');
            
            res.redirect('/');
        })
    })
});

module.exports = router;