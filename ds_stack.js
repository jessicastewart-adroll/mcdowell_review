function balanceBrackets(expression) {
    let pairs = {'(': ')', '{': '}', '[':']'},
        closing = [')', '}', ']']
        holder = []
    
    for (let i = expression.length - 1; i > -1; i--) {
        if (closing.includes(expression[i])) {
            holder.push(expression[i])
        } else if (Object.keys(pairs).includes(expression[i])) {
            let match = holder.pop()
            if (match != pairs[expression[i]]) {
                console.log("NO")
                return
            }
        }
    }
    
    if (holder.length != 0) {
      console.log("NO")
    } else {
      console.log("YES")
    }
}
