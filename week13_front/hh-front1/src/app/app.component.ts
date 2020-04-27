import {Component} from '@angular/core';
import {CompanyService} from './services/company.service';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent {
    title = 'hh-front';


    logged = false;

    username = 'alibek';
    password = 'AAA';

    constructor(private companyService: CompanyService) {
    }
    login() {
        this.companyService.login(this.username, this.password)
            .subscribe(res => {

                localStorage.setItem('token', res.token);

                this.logged = true;

                this.username = '';
                this.password = '';
            });
    }

    logout() {
        localStorage.clear();
        this.logged = false;
    }
}
