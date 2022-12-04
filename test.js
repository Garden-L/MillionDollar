function func2 () {
    console.log(this);
}
a = {};

a.b = 10;
a.func = function () {
    d = {
        r : this.b,
    }
    console.log(d.r);
    return this.b;
}


console.log(a.func());