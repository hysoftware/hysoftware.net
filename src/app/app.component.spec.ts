import { TestBed, async } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AppComponent } from './app.component';

describe('AppComponent', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [
        RouterTestingModule
      ],
      declarations: [
        AppComponent
      ],
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should have as misc the list of misc links', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app.misc).toEqual([
      {
        icon: 'fas fa-file-pdf',
        link: '../assets/resume.pdf',
        name: 'Resume (PDF)'
      },
      {
        icon: 'fas fa-file-code',
        link: 'https://github.com/hysoftware/hysoftware.net',
        name: 'Code of This Page'
      }
    ]);
  });

  it(`should have as snsList the list of my sns`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app.snsList).toEqual([
      {
        icon: 'fab fa-github',
        link: 'https://github.com/hiroaki-yamamoto',
        name: 'Github',
      },
      {
        icon: 'fab fa-gitlab',
        link: 'https://gitlab.com/hiroaki-yamamoto',
        name: 'Gitlab',
      },
      {
        icon: 'fab fa-linkedin',
        link: 'https://www.linkedin.com/in/hyamatan',
        name: 'Linkedin'
      },
      {
        icon: 'fab fa-angellist',
        link: 'https://angel.co/hiroaki-yamamoto',
        name: 'Angel List'
      },
      {
        icon: 'fab fa-keybase',
        link: 'https://keybase.io/hyamamoto',
        name: 'Keybase'
      }
    ]);
  });
});
