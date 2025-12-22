import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LinkListComponent } from './link-list.component';
import { LinkList } from '../link-list';

describe("Link List Component", () => {
  let component: LinkListComponent;
  let fixture: ComponentFixture<LinkListComponent>;
  let correct: LinkList;
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LinkListComponent]
    })
      .compileComponents();

    fixture = TestBed.createComponent(LinkListComponent);
    component = fixture.componentInstance;
    correct = TestBed.inject(LinkList);
    await fixture.whenStable();
  });

  it("The component field 'links' should be same as LinkList.", () => {
    expect(component.links).toStrictEqual(correct)
  });
});
