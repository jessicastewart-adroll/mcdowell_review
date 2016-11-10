/*
enqueue: add element to end
dequeue: remove element from front

*create queue using 2 stacks
  1 enqueue
  2 dequeue
  3 print first
  
*input: line count, operation number, element
/*
function processData(input) {
    let Queue = function() {
        this.firstQueue = [];
        this.secondQueue = [];
    }

    Queue.prototype.enqueue = function(element) {
      this.firstQueue.push(element);
    }

    Queue.prototype.dequeue = function() {
      while (this.firstQueue.length > 1) {
        let temp = this.firstQueue.pop();
        this.secondQueue.push(temp);
      }
  
      let final = this.firstQueue.pop();
  
      while (this.secondQueue.length > 0) {
        let temp = this.secondQueue.pop();
        this.firstQueue.push(temp);
      }
  
      return final;
    }

    Queue.prototype.peek = function() {
      if (this.firstQueue.length > 0) {
        console.log(this.firstQueue[0]);
      };
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
