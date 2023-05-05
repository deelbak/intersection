import { Component } from '@angular/core';
import {District} from '../models'
import {DistrictService} from "../district.service";

@Component({
  selector: 'app-districts',
  templateUrl: './districts.component.html',
  styleUrls: ['./districts.component.css']
})
export class DistrictsComponent {
  districts: District[] = [];
  newDistrict: string = '';
  logged: boolean = false;
  username: string = '';
  password: string = '';

  constructor(private districtService: DistrictService) {
  }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
      this.getDistricts();
    }

  }

  getDistricts() {
    this.districtService.getDistricts().subscribe((districts) => {
      this.districts = districts;
    });
  }


  addDistrict() {
    this.districtService.createDistrict(this.newDistrict).subscribe((district) => {
      this.districts.push(district);
      this.newDistrict = '';
    });
  }

  deleteDistrict(districts_id: number) {
    this.districtService.deleteDistrict(districts_id).subscribe((data) => {
      this.districts = this.districts.filter((districts) => districts.id !== districts_id);
    });
  }

}
