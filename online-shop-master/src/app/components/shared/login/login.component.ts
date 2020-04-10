import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username: string;
  password: string;
  constructor() { }

  ngOnInit(): void {
  }
  LoginUser(){
    if (this.username == "Nurgissa" && this.password == "123"){
      alert("Welcome, Nurgissa");
    } else{
      alert("Incorrect data")
    }
    {

    }
  }

}
