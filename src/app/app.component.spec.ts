import { TestBed } from '@angular/core/testing';

import { MatButtonModule } from '@angular/material/button';
import { MatTabsModule } from '@angular/material/tabs'
import { MatTableModule } from '@angular/material/table';

import { AppComponent } from './app.component';
import { DeadComponent } from './dead/dead.component';
import { NormalComponent } from './normal/normal.component';
import { LinksComponent } from './links/links.component';
import { JPASCTComponent } from './jpasct/jpasct.component';

describe('AppComponent', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        MatButtonModule,
        MatTabsModule,
        MatTableModule,
      ],
      declarations: [
        AppComponent,
        DeadComponent,
        LinksComponent,
        NormalComponent,
        JPASCTComponent,
      ],
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app).toBeTruthy();
  });
});
