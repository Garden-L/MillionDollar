const User          = require('../models/user');
const crypto        = require('crypto');
const passport      = require('passport');
const localStrategy = require('passport-local');

//util
const getPbkdf2     = require('../util/getPbkdf2');

module.exports = () => {
    passport.use(new localStrategy({
        usernameField: 'id',
        passwordField: 'password',
    }, async (id, password, done) => {
        try{
            const exUser = await User.findOne({where: {id}, rejectOnEmpty: false});
            
            if(exUser) {
                const pswTosha = await getPbkdf2 (password, exUser.salt, 10908, 64, 'sha256');
                const result = pswTosha.toString('Base64');

                if(exUser.password == result){
                    console.log('비밀번호 일치');
                    done(null, exUser);
                } else {
                    console.log('불일치');
                    console.log(result);
                    console.log(exUser.password);
                    done(null, false, {message : '비밀번호가 불일치 합니다'});
                }
            } else {
                done(null, false, { message : '가입되지 않은 회원 입니다'});
            }
        } catch (err){
            console.log(err);
            done(err);
        }
    }));
};