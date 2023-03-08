import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LinksComponent } from './links.component';
import { faFileCode, faFilePdf } from '@fortawesome/free-solid-svg-icons';
import { faGithub, faGitlab, faKeybase } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

describe('LinksComponent', () => {
  let component: LinksComponent;
  let fixture: ComponentFixture<LinksComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [FontAwesomeModule],
      declarations: [LinksComponent],
    }).compileComponents();
  });

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
        icon: faFileCode,
        link: 'https://github.com/hysoftware/hysoftware.net',
        name: 'Code of This Page'
      },
      {
        icon: faFilePdf,
        link: 'https://www.canva.com/design/DADks8eRENo/4npkcNMd5b5OSyFNTXXMvw/view',
        name: 'Resume about me'
      }
    ]);
  });

  it(`should have as snsList the list of my sns`, () => {
    const app = fixture.debugElement.componentInstance;
    expect(app.snsList).toEqual([
      {
        icon: faGithub,
        link: 'https://github.com/hiroaki-yamamoto',
        name: 'Github',
      },
      {
        icon: faGitlab,
        link: 'https://gitlab.com/hiroaki-yamamoto',
        name: 'Gitlab',
      },
      {
        icon: faKeybase,
        link: 'https://keybase.io/hyamamoto',
        name: 'Keybase'
      }
    ]);
  });
});
