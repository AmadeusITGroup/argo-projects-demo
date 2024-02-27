import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root',
})
export class PetService {

    private petUrl= 'http://app-prod-my-app.127.0.0.1.nip.io/pet';

    private httpOptions = {
        responseType: 'text'
    };

    constructor(private http: HttpClient) { }

    getPet(): Observable<String> {
        return this.http.get(this.petUrl, {
            headers: new HttpHeaders({
                'Accept': 'text/html, application/xhtml+xml, */*',
                'Content-Type': 'application/x-www-form-urlencoded'
              }),
              responseType: 'text'
            });
    }
}