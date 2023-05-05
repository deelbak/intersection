import {Component, OnInit} from '@angular/core';
import {District} from './models'
import {DistrictService} from "./district.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  title = 'inters_front';

  logged: boolean = false;
  username: string = '';
  password: string = '';

  constructor(private districtService: DistrictService) {
  }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
      
    }

  }

  

  login() {
    this.districtService.login(this.username, this.password).subscribe((data) => {
      localStorage.setItem('token', data.token);
      this.logged = true;
      this.username = '';
      this.password = '';
      
    });
  }

  logout() {
    localStorage.removeItem('token');
    // Request to the Django
    this.logged = false;
  }

 
}