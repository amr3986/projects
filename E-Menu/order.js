
function drinkON(){
      document.getElementById("drink-box").style.display="block";} 

function drinkOFF(){
  document.getElementById("drink-box").style.display="none";}



function FoodType(){

  var type = document.getElementById("foodselect").value;
  
  switch(type) {
    case "SeaFood":
      document.getElementById("dishes").innerHTML=
      "<option>Shrimp Creole</option>\
      <option >Fish Tacos with Lime</option>\
      <option >Glazed salmon</option>\
      <option >Tuna noodels</option>\
      <option >Labstor with lemon</option>";
      break;
    case "Indian Food":
      document.getElementById("dishes").innerHTML=
      "<option>Indian Spiced Chicken</option>\
      <option >Tandoori Chicken</option>\
      <option >Mughlai Biryani</option>\
      <option >Punjabi Chickpea Curry</option>\
      <option >Fish Curry</option>";
      break;
      case "Fast Food":
        document.getElementById("dishes").innerHTML=
    "<option>Chicken burger meal</option>\
    <option >Chicken nuggets meal</option>\
    <option >Meat burger meal</option>\
    <option >Chicken fingers</option>\
    <option >Chicken sandwich</option>";
      break;
      case "Healthy Food":
        document.getElementById("dishes").innerHTML=
        "<option>Vegetable Noodle Soup</option>\
        <option >Quinoa Salad</option>\
        <option >Chicken and Broccoli</option>\
        <option >Oven-Baked Salmon</option>\
        <option >Fettuccine Alfredo</option>";
      break;
      case "Arabian Food":
        document.getElementById("dishes").innerHTML=
        "<option>Mandi Chicken</option>\
        <option >Meat kabab</option>\
        <option >Mahashi</option>\
        <option >Moussaka</option>\
        <option >Lamb mandi</option>";
        break;
    
  }   
 
}

function ThankYou(){
alert("Your order has been submitted\n Thank you");
window.location = '/E-menu/Home.html';
}

