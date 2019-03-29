import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LinksComponent } from './links.component';

describe('LinksComponent', () => {
  let component: LinksComponent;
  let fixture: ComponentFixture<LinksComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LinksComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LinksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have as misc the list of misc links', () => {
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
