import { TestBed } from '@angular/core/testing';

import { LinkList } from './link-list';
import { faFileCode, faFile } from '@fortawesome/free-solid-svg-icons';
import { faGithub, faGitlab, faKeybase } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

describe('LinkList', () => {
  let service: LinkList;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [FontAwesomeModule],
    });
    service = TestBed.inject(LinkList);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
  it('Should have snsList with proper link order', () => {
    expect(service.snsList).toStrictEqual([
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
  it('Should have misc with proper link order', () => {
    expect(service.miscList).toStrictEqual([
      {
        icon: faFileCode,
        link: 'https://github.com/hysoftware/hysoftware.net',
        name: 'Code of This Page'
      },
      {
        icon: faFile,
        link: 'https://www.canva.com/design/DADks8eRENo/4npkcNMd5b5OSyFNTXXMvw/view',
        name: 'Resume about me'
      },
    ]);
  });
});
