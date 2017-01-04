/*Create an object that has several converter methods:

float2string(num) it should convert a float number to a string, for example 12.24 -> '12.24'
string2float(str) it should convert a string to a float number, for example '12.24' -> 12.24
int2roman(number) it should convert an int number to a roman number as a string, for example 12 -> 'XII'
roman2int(number) it should convert a roman number as a string to an int, for example 'XII' -> 12 please try to avoid using the built in conversion methods*/

var convert = {

  romans : {
    0: ['', 'I',	'II',	'III',	'IV', 'V', 'VI',	'VII', 'VIII',	'IX'],
    1: ['', 'X',	'XX', 'XXX',	'XL',	'L', 'LX',	'LXX',	'LXXX',	'XC'],
    2: ['', 'C',	'CC',	'CCC',	'CD',	'D',	'DC',	'DCC',	'DCCC',	'CM'],
    3: ['', 'M',	'MM',	'MMM',	'MV',	'V',	'VM',	'VMM',	'VMMM',	'MX']},

  float2string : function(num){
    num = String(num);
    return num;
  },
  string2float : function(string){
    string = parseFloat(string);
    return string;
  },
  int2roman : function(number){
    number = String(number).split("");
    number.reverse();
    var roman = [];
    for (var i = number.length-1; i >= 0; i--){
      console.log(number[i]);
      if (number[i] != undefined){
        roman.push(this.romans[i][number[i]]);
      }
    }
    var roman2 = roman.join('');
    return roman2;
  }
  //roman2int : function(number){};
};

console.log(convert.float2string(4.5));
console.log(convert.string2float('5'));
console.log(convert.int2roman(255));
console.log(convert.int2roman(2192));
