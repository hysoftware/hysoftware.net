import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { MatButtonModule } from '@angular/material/button';
import { MatTabsModule } from '@angular/material/tabs'
import { MatTableModule } from '@angular/material/table';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from './app.component';
import { VulModule } from './vul/vul.module';
import { NormalComponent } from './normal/normal.component';
import { LinksComponent } from './links/links.component';
import { DeadComponent } from './dead/dead.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { JPASCTComponent } from './jpasct/jpasct.component';

@NgModule({
  declarations: [
    AppComponent,
    NormalComponent,
    LinksComponent,
    DeadComponent,
    JPASCTComponent
  ],
  imports: [
    BrowserModule,
    VulModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatTabsModule,
    MatTableModule,
    FontAwesomeModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
