/*
enqueue: add element to end
dequeue: remove element from front

*create queue using 2 stacks
  1 enqueue
  2 dequeue
  3 print first
  
*input: line count, operation number, element
*/

function processData(input) {
    let Queue = function() {
        this.input = [];
        this.output = [];
    }

    Queue.prototype.enqueue = function(element) {
      this.input.push(element);
    }

    Queue.prototype.dequeue = function() {
      if (this.output.length === 0) {
        while (this.input.length != 0) {
            this.output.push(this.input.pop());
        }
      }
      return this.output.pop();
    }

    Queue.prototype.peek = function() {
      if (this.output.length === 0) { // prevent pushing new elements in incorrect order
        while (this.input.length != 0) {
            this.output.push(this.input.pop());
        }
      }
      console.log(this.output[this.output.length-1]);
    }
    
    commandKey = {
        '1': 'enqueue',
        '2': 'dequeue',
        '3': 'peek'
    }; 
    let commands = input.split('\n');
   
    q = new Queue()
    for (let i = 1; i < commands.length; i++) {
        let command = commands[i].split(' ') [0],
            element = commands[i].split(' ') [1];
        if (command === '1') {
            q.enqueue(parseInt(element));
        } else if (command === '2') {
            q.dequeue();
        } else if (command === '3') {
            q.peek();
        }
    }
}

// execute in Node environment
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
