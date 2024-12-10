//switch case
function a(a){
    switch (typeof a){
        case ("number"):
            console.log("integer");
            break;
        
        case ('string'):
            console.log("string");
            break;
        case ('boolean'):
            console.log("boolean");
            break;
      
    
}


}

//ternery operator
function b(age){
    msg=(age>=18)? "adult":"minor"
    console.log(msg);
}

//WAP to assign grade for a student For example, if the score is between 90 and 100, assign the grade "A.", (take score of every subject as input).
function c(score){
    if (90<=score&&score<100){
        return "A";
    }
    else if (80<=score||score<90){
        return "B";
    }
    else if (40<=score<80){
        return "C";
    }
    else {
        return "fail"
    }
}

//WAP that classifies a number as positive, negative, even, or odd.


function d(num){
    if (num>0){
        console.log(num);
        if (num/2){
             console.log("odd and positive");
        }
        else{
            console.log("even and positive");
        }
       
    }
    else{
        console.log(num);
        if (num/2){
            console.log("odd and negative");
        }
        else{
            console.log("even and negative");
        }
       
    }
}



//WAP to validate a username. If the username is less than 6 characters, log "Username too short"; if it's more than 15 characters, log "Username too long"; otherwise, log "Username accepted."
//6-15 ok
function e(na){
    console.log(na);

    x=na.length
    console.log(x); 
    if (x<6){
        console.log("name too short");
    }
    else{
        if (x>6 && x<15){
            console.log("username ok");
        }
        else{
            console.log("name too loong");
        }
    }
    

}


//1
function f(num){

    if (num>0){
        console.log(num);
        console.log(num%2);
        // if (num/2){
        //      console.log("odd and positive");
        // }
        // else{
        //     console.log("even and positive");
        // }
        msg=(num%2)?"odd and positive":"even and positive"
        console.log(msg);
    }
    else {
        console.log(num);
        console.log(num%2);
        // if (num/2){
        //     console.log("odd and negative");
        // }
        // else{
        //     console.log("even and negative");
        // }
        msg=(num%2)?"odd and negative":"even and negative"
        console.log(msg);
    }
}
