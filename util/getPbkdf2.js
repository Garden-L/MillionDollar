const crypto = require('crypto');

function getPbkdf2 (password, salt, iterator, keylen, digest){
    return new Promise((resolve, reject) => {
        crypto.pbkdf2(password, salt, iterator, keylen, digest, function (err, derivedKey){
            if(err) {
                reject(err);
            } else{
                resolve(derivedKey);
            }
        })
    });
}

module.exports = getPbkdf2;