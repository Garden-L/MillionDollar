const passport  = require('passport');
const local     = require('./localStrategy');
const User      = require('../models/user');

module.exports = function init (){
    passport.serializeUser((user, done) => {
        console.log(user);
        done(null, user.id);
    });

    passport.deserializeUser(async (id, done) => {
        try{
            const user = await User.findOne({where : {id},
            rejectOnEmpty: true});
            
            done(null, user);
                
        } catch(err){
            done(err);
        }
    })

    local();
}