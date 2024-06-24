function randNote(){

    var index = Math.floor(Math.random() *13);

    if(index == 0){

        return(randNote());


    }




    //console.log(index.toString());

    return index;


    }


    function randFile(index){

    if(index == 1){

        return("anatural.mp3");
    }
    else if (index == 2){

        return("asharp.mp3");
    }

    else if (index == 3){

        return("bflat.mp3");
    }

    else if (index == 4){

        return("bnatural.mp3");
    }

    else if (index == 5){

        return("c.mp3");
    }

    else if (index == 6){

        return("csharp.mp3");
    }
    else if (index == 7){

        return("dnatural.mp3");
    }

    else if (index == 8){

        return("dsharp.mp3");
    }
    else if (index == 9){

        return("enatural.mp3");
    }
    else if (index == 10){

        return("fnatural.mp3");
    }

    else if (index == 11){

        return("fsharp.mp3");


    }
    else if (index == 12){

        return("gnatural.mp3");


    }

    else if (index == 13){

        return ("gsharp.mp3");


    }

    }


    function myFunction(){
        const obj = randFile(randNote());
        var audio = new Audio('static/music/'+obj);
        console.log(obj);
        audio.play();
       // button.disabled = true;
    }

myFunction();