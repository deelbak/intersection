import {Injectable} from '@angular/core';
import {Observable} from "rxjs";
import {AuthToken, District} from "./models";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class DistrictService {

  BASE_URL = 'http://localhost:8000'

  constructor(private client: HttpClient) {
  }

  login(username: string, password: string): Observable<AuthToken> {
    return this.client.post<AuthToken>(
      `${this.BASE_URL}/api/login/`,
      {username, password}
    )
  }

  getDistricts(): Observable<District[]> {
    return this.client.get<District[]>(
      `${this.BASE_URL}/api/districts/`
    )
  }

  createDistrict(districtName: string): Observable<District> {
    return this.client.post<District>(
      `${this.BASE_URL}/api/districts/`,
      {name: districtName}
    )
  }

  deleteDistrict(district_id: number): Observable<any> {
    return this.client.delete(
      `${this.BASE_URL}/api/districts/${district_id}/`
    )
  }
}