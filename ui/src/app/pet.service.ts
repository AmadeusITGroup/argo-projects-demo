import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root',
})
export class PetService {

    private petUrl= 'http://app-prod-my-app.127.0.0.1.nip.io/pet';

    constructor(private http: HttpClient) { }

    getPet(): Observable<String> {
        return this.http.get(this.petUrl, {
            responseType: 'text'
        });
    }
}