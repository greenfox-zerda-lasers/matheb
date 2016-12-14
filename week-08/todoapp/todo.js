var task = {};

function askInputValue(){
  var newInput = document.querySelector('input').value;
  var data = new FormData(newInput);
  return data;
};

function askTodoListLength(){
  var askLength = new XMLHttpRequest();
  askLength.open('GET', "https://mysterious-dusk-8248.herokuapp.com/todos", true);
  askLength.setRequestHeader("Content-Type: application/json");
  askLength.send();
  if (askLength.readyState === XMLHttpRequest.DONE){
    var TodoList = JSON.parse(askLength.response);
    var Listlength = TodoList.length;
    return Listlength;
  }
};

function addTodoItem(){
  task['id'] = askTodoListLength()-1;
  task['text'] = askInputValue();
  task['completed'] = 'false';
  var req = new XMLHttpRequest();
  request.open('POST', "https://mysterious-dusk-8248.herokuapp.com/todos", true);
  request.setRequestHeader("Content-Type: application/json");
  req.send(JSON.stringify(task));
  //itt növelődik a lista div magassága + kerül bele a tartalom !!!!!
};

//function delTodoItem(){};

//function checkingTask(){};
  //checkbox színe
  //Completed status change
